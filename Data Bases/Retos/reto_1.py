def sum_gits(number):
    total = 0
    sumText = ""
    try:
        for d in str(number):
            total += int(d)
            if (sumText != ""):
                sumText += "+"
            sumText += f"{d}"
    except Exception as e:
        print(f"Error: {e}")
        return
    print(f"{sumText}={total}")


def main():
    number = 123456789
    sum_gits(number)

if __name__ == "__main__":
    main()