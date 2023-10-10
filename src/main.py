import openai

from answer import AnswerQuestionUseCase
from embedding import BuildEmbeddingUseCase

# OpenAIのAPIキーを設定する。
openai.api_key = "YOUR_API_KEY"

# STEP1: テキストを分散表現に変換する。
BuildEmbeddingUseCase().execute(
    text_dir_path="text/article",
    text_embeddings_file_path="embeddings/abstract_and_conclusion_001.csv"
)

# STEP2: テキストに対して質問を投げかけ、回答を得る。
answer = AnswerQuestionUseCase().execute(
    text_embeddings_file_path="embeddings/abstract_and_conclusion_001.csv",
    question="What are some terms related to nutrition? Pull out the numbers along with the term."
)
print(f"Answer: {answer}")
