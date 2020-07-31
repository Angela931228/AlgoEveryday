def gcs(a, b):
    if a == 0 :
        return b
    return gcs(b%a, a)

print(gcs(48, 36))