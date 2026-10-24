def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores)


def main() -> None:
    text = input("請輸入成績，以空白分隔：")
    
    try:
        scores = [float(item) for item in text.split()]
    except ValueError:
        print("請輸入有效數字。")
        return

    if not scores:
        print("請至少輸入一個成績。")
        return

    average = calculate_average(scores)
    print(f"平均分數：{average:.2f}")


if __name__ == "__main__":
    main()