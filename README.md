### プロジェクト概要

このプロジェクト「回答キッド」は、OpenAI APIを使用した質疑応答機能を実装するプロジェクトです。  
あらかじめ用意したテキストに対して質問を投げかけ、回答を得ることができます。

主なステップは以下の通りです。
1. テキストを分散表現に変換する。
2. テキストに対して質問を投げかけ、回答を得る。

また、OpenAIの公式サンプルである[openai-quickstart-python](https://github.com/openai/openai-quickstart-python)を参考にしています。  
quickstartでは、WEBサイトをスクレイピングしてテキストを入手することを前提としていますが、  
このプロジェクトでは分散表現への変換から質疑までの一連のプロセスをユースケースとして整理し、  
より汎用的な目的で利用できるようインターフェースを改良しています。

How to build an AI that can answer questions about your website  
https://platform.openai.com/docs/tutorials/web-qa-embeddings

### 注意事項

* このプロジェクトを実行するには、OpenAI APIキーが必要です。  
APIキーを取得するには、[OpenAIのウェブサイト](https://platform.openai.com/overview)でサインアップしてください。  
初回登録時に$18分のクレジットが付与されるのでテストが可能です。

### インストール方法

1. リポジトリをクローンします。Clone the repository.
2. Python仮想環境を構築します。Build the python virtual environment.

```
$ python -m venv venv
$ venv/Scripts/activate
```

2. 必要なPythonパッケージをインストールします。Install the required Python packages.

```
$ python -m pip install -r requirements.txt
```

### 使用方法

1. OpenAIのウェブサイトにアクセスしAPIキーを取得します。  
画面右上のプロフィールメニューのView API Keysより取得できます。

2. 取得したAPIキーを`src/main.py`に設定します。

```
openai.api_key = "YOUR_API_KEY"
```

3. テキストファイルを`text/{something}/*.txt`の形で配置します。

```
text/article/abstract_and_conclusion.txt
(例)論文の内容に関する質問をする場合、対象となる論文のテキストを配置します。
```

4. `src/main.py`を編集し、テキストのディレクトリパスと質問を設定します。

```
# STEP1: テキストを分散表現に変換する。
BuildEmbeddingUseCase().execute(
    text_dir_path="text/article",
    embeddings_file_path="embeddings/abstract_and_conclusion.csv"
)

# STEP2: テキストに対して質問を投げかけ、回答を得る。
answer = AnswerQuestionUseCase().execute(
    embeddings_file_path="embeddings/abstract_and_conclusion.csv",
    question="What words or idioms are related to physical frailty?"
)
print(f"Answer: {answer}")
```

5. `src/main.py`を実行し、回答を得ます。

```
$ python src/main.py
Answer:  Weakness, slowness, reduced muscle mass, loss of muscle strength, ...
```

### 考えられる応用例として

* チャットボットの構築
* ナレッジシステムの意味検索
* 電子書籍との対話

### 使用しているAPIの紹介

※個人的な理解によるもので間違っている可能性があります。

API Reference - Embeddings  
https://platform.openai.com/docs/api-reference/embeddings

Embedding(分散表現、埋め込みとも)とは、テキストをベクトルに変換するための手法のことです。  
意味が似ている単語は近く、似ていない単語は遠くなるように、各単語にベクトルを振り分けます。  
テキストを分散表現に変換するために、Glove、BERT、ELMoなどのモデルが使用できます。

自然言語処理モデルに、コンテキストとして与えられるトークン数に制限があるため、  
あらかじめ用意したテキストの文と質問の分散表現の類似度を計算し、  
コンテキストとして使用する文を絞り込むために利用します。

API Reference - Create completion  
https://platform.openai.com/docs/api-reference/completions/create

コンテキストを与えて質問の回答を得るために使用します。
