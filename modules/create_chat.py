from openai import OpenAI
from dotenv import load_dotenv;load_dotenv()

def create_chat(string: str) -> str:

  client = OpenAI()
  schema = {
    "会社名": "string",
    "部署名": "string",
    "氏名": "string",
    "会社住所": "string | null",
    "電話番号": "string | null",
    "e-mailアドレス": "string | null",
  }

  response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    response_format={ "type": "json_object" },
    messages=[
      {"role": "system", "content": f"次の文字列から会社名、部署名、氏名、会社住所、電話番号、e-mailアドレスを抜き出して、JSON形式で出力してください。JSONのスキーマは次の通りです：{schema}。氏と名の間には半角スペースを入れてください。会社住所に郵便番号が含まれている場合は郵便番号を先頭に記述してください。〒という記号が入っている場合は除去してください。電話番号に数字以外の記号が入っている場合は全て半角ハイフンに置換してください。"},
      {"role": "user", "content": string}
    ]
  )

  return response
