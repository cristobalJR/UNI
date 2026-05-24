def merge(left, right):
    i = 0
    j = 0
    ll = len(left)
    lr = len(right)
    result = [None] * (ll + lr)
    k = 0

    while i < ll and j < lr:
        if left[i][1] <= right[j][1]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while i < ll:
        result[k] = left[i]
        i += 1
        k += 1

    while j < lr:
        result[k] = right[j]
        j += 1
        k += 1

    return result


def closestPair(lo, hi):
    size = hi - lo

    if size <= 3:
        best_d = INF
        best_pts = set()

        for i in range(lo, hi):
            xi = pts[i][0]
            yi = pts[i][1]

            for j in range(i + 1, hi):
                dx = xi - pts[j][0]
                dy = yi - pts[j][1]
                d = dx * dx + dy * dy

                if d < best_d:
                    best_d = d
                    best_pts = {pts[i], pts[j]}
                elif d == best_d:
                    best_pts.add(pts[i])
                    best_pts.add(pts[j])

        sub_by_y = sorted(pts[lo:hi], key=lambda p: p[1])
        return best_d, best_pts, sub_by_y

    mid = (lo + hi) // 2
    midx = pts[mid][0]

    d_l, pts_l, by_y_l = closestPair(lo, mid)
    d_r, pts_r, by_y_r = closestPair(mid, hi)

    by_y = merge(by_y_l, by_y_r)

    if d_l < d_r:
        d = d_l
        result_pts = set(pts_l)
    elif d_r < d_l:
        d = d_r
        result_pts = set(pts_r)
    else:
        d = d_l
        result_pts = pts_l | pts_r

    strip = []

    for p in by_y:
        dx = p[0] - midx
        if dx * dx <= d:
            strip.append(p)

    m = len(strip)

    for i in range(m):
        xi = strip[i][0]
        yi = strip[i][1]

        for j in range(i + 1, m):
            dy = strip[j][1] - yi

            if dy * dy > d:
                break

            dx = xi - strip[j][0]
            dd = dx * dx + dy * dy

            if dd < d:
                d = dd
                result_pts = {strip[i], strip[j]}
            elif dd == d:
                result_pts.add(strip[i])
                result_pts.add(strip[j])

    return d, result_pts, by_y


n = int(input())
pts = []

for _ in range(n):
    x, y = map(int, input().split())
    pts.append((x, y))

pts.sort()

INF = float("inf")

min_d_sq, result_pts, _ = closestPair(0, n)

result_list = sorted(result_pts)
dist = min_d_sq ** 0.5

out = ["Distancia: " + format(dist, ".2f")]

for p in result_list:
    out.append("(" + str(p[0]) + ", " + str(p[1]) + ")")

print("\n".join(out))