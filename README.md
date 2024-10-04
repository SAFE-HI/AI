
---

# 안심하이 AI 모듈

## 프로젝트 개요

안심하이 AI 모듈은 **고독사 위험군**을 식별하고, 이를 돕기 위한 **맞춤형 질문 생성** 및 **상담 보조** 기능을 제공합니다. 이를 통해 상담자는 효율적으로 고위험군을 파악하고, 적절한 조치를 취할 수 있습니다. 주요 기능으로는 **생성형 AI**를 활용한 체크리스트 질문 생성과 **STT(Speech-to-Text)** 기반의 실시간 대화 요약 기능이 포함됩니다.

## 주요 기능

### 1. 체크리스트 질문 생성
- **ChatGPT** 모델을 이용하여 고독사 위험군을 식별하는 맞춤형 질문을 자동으로 생성합니다.
- 상담자는 이러한 질문을 통해 더욱 효율적으로 위험군을 파악하고 적절한 대응을 할 수 있습니다.

### 2. 실시간 상담 보조
- 상담 중 녹음된 음성을 **STT** 기능을 통해 실시간으로 텍스트로 변환합니다.
- 변환된 텍스트는 자동으로 요약되어 상담자가 대화의 핵심 내용을 빠르게 파악할 수 있습니다.

### 3. 감정 분석을 통한 심리 상태 평가
- **감정 분석** 모델을 통해 대화 중 대상자의 심리적 상태를 분석하여, 대상자의 현재 상태에 대한 추가적인 정보를 제공합니다.

## 디렉토리 구조

```
├── AI
│   ├── ai_api.js                  # AI API 호출 및 처리
│   └── funcs
│       ├── call_ai_func_using_localfunc.js  # 로컬 AI 함수 호출
│       ├── call_ai_func_using_web.js        # 웹 기반 AI 함수 호출
│       └── index.js                         # AI 함수 실행 로직
├── 안심하이 STT 및 요약.ipynb               # STT 및 요약 처리 Jupyter 노트북
├── 안심하이_감정분석.ipynb                   # 감정 분석 관련 Jupyter 노트북
├── 안심하이_대화가이드라인.ipynb             # 대화 가이드라인 생성 Jupyter 노트북
└── README.md                                 # 프로젝트 설명 파일
```

## 설치 및 설정

### 1. 필수 라이브러리 설치

다음의 명령어를 통해 필요한 라이브러리를 설치할 수 있습니다.

```bash
# Node.js 모듈 설치
npm install openai axios express

# Python 라이브러리 설치
pip install openai pydub requests
```

### 2. 환경 변수 설정

OpenAI API를 사용하기 위해서는 환경 변수를 설정해야 합니다. `OPENAI_API_KEY`를 설정하세요.

```bash
# 환경 변수 설정 (예시: Linux/MacOS)
export OPENAI_API_KEY=your_openai_api_key

# 환경 변수 설정 (Windows)
set OPENAI_API_KEY=your_openai_api_key
```

## 사용법

### 1. 체크리스트 질문 생성

`ai_api.js` 파일 내에 정의된 API를 호출하여 고독사 위험군 체크리스트 질문을 생성할 수 있습니다.

```javascript
const openai = require('openai');

async function generateQuestion(topic) {
  const response = await openai.Completion.create({
    model: "gpt-3.5-turbo",
    prompt: `Create a checklist to identify high-risk individuals for ${topic}.`,
    max_tokens: 500
  });

  return response.choices[0].text;
}
```

### 2. STT 및 텍스트 요약

`안심하이 STT 및 요약.ipynb` 파일에서 녹음된 음성을 STT로 변환하고, 텍스트 요약을 실행합니다.

```python
import openai

def summarize_text(content):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Summarize the following conversation: {content}",
        max_tokens=100
    )
    return response.choices[0].text.strip()
```

## API 사용 예시

### 1. 질문 생성 API

```http
POST /ai/generate_question
```
- **설명**: 고독사 위험군 식별을 위한 질문을 생성합니다.
- **Request Body**:
```json
{
  "topic": "elderly care"
}
```
- **Response**:
```json
{
  "question": "What is your current living situation, and do you feel isolated?"
}
```

### 2. STT 변환 및 요약 API

```http
POST /ai/stt_summarize
```
- **설명**: 상담 내용을 실시간으로 STT로 변환하고 요약합니다.
- **Request Body**:
```json
{
  "audio": "base64_encoded_audio"
}
```
- **Response**:
```json
{
  "summary": "The client feels isolated and needs regular assistance."
}
```

## 향후 계획
- AI 질문 생성 모델을 고도화하여 더 다양한 고독사 위험군을 효과적으로 식별할 수 있는 기능을 추가할 예정입니다.
- 감정 분석 기능을 고도화하여 실시간 심리 상태 파악 및 자동 대응 시스템을 구현할 계획입니다.
- 상담 기록 데이터를 기반으로 한 맞춤형 복지 서비스 추천 시스템을 추가할 예정입니다.

---
