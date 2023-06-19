def calculate_lucky_tickets(n, k, m):
    def f(total, r, k):
        ans = ((pow(k - 1, n, m) - (-1) ** n) * pow(k, -1, m)) % m
        if (r * n - total) % k == 0:
            ans += (-1) ** n
        return ans

    ans = 0

    if k % 2 == 1:
        for i in range(k):
            ans += pow(k, n - 1, m) - f(2 * i, i, k)
    else:
        for i in range(k // 2):
            ans += pow(k, n - 1, m) - f(2 * i, i, k // 2) * pow(2, n - 1, m)

    return ans % m


n, k, m = map(int, input().split())
result = calculate_lucky_tickets(n, k, m)
print(result)
