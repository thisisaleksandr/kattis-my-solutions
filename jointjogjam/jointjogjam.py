kx, ky, ox, oy, ekx, eky, eox, eoy = map(int, input().split())
absdist_st = ((kx-ox)**2 + (ky-oy)**2)**0.5
absdist_end = ((ekx-eox)**2 + (eky-eoy)**2)**0.5
print(max(absdist_st, absdist_end))