# 测试

## 安装 ollama

```sh
brew install ollama
ollama pull llama3.2:1b
ollama serve # 启动 ollama
```

## 安装依赖

```sh
make venv/init
source bin/activate
make deps
```


## 运行

```sh
make run/test # python scripts/test.py
```
