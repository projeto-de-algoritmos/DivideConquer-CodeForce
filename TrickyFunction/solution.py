def closest_pair(points):

    assert len(points) >= 2
    initial_distance = abs(points[0] - points[1])
    closest_pair = (0, 1)
    grid = {}

    for i, point in enumerate(points):
        fx = int(point.real / initial_distance)
        fy = int(point.imag / initial_distance)

        grid.setdefault((fx, fy), []).append(i)

        current_distance = initial_distance
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx = fx + dx
                ny = fy + dy

                if (nx, ny) in grid:
                    for j in grid[(nx, ny)]:
                        if i == j:
                            continue

                        distance = abs(points[i] - points[j])
                        if current_distance > distance:
                            current_distance = distance
                            closest_pair = (i, j)

        if current_distance < initial_distance:
            initial_distance = current_distance
            for j in range(i + 1):
                p = points[j]
                fx = int(p.real / initial_distance)
                fy = int(p.imag / initial_distance)

                grid.setdefault((fx, fy), []).append(j)

    return closest_pair

N = int(input())
As = list(map(int, input().split()))

points = []
y = 0

for i in range(N):
    y += As[i]
    points.append(complex(i, y))

i, j = closest_pair(points)
distance_squared = int(abs(points[i] - points[j]) ** 2 + 0.5)
print(distance_squared)
