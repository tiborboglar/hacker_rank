# Complete the repeatedString function below.
def repeatedString(s, n):
    quociente = n // len(s)
    quociente_count = s.count('a')*quociente

    resto = n % len(s)
    resto_count = s[:resto].count('a')

    count = quociente_count + resto_count
    return count