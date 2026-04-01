from src.injector import inject
from src.analyzer import analyze

def main():
    prompt = "Hello"
    injected = inject(prompt)
    result = analyze(injected)
    print(result)

if __name__ == "__main__":
    main()
