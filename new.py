# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?

total=int(input("Сколько км надо проехать машине? "))
one_day=int(input("Сколько км проезжает машина в день? "))
days = (total+one_day-1)//one_day
print("1.Чтобы проехать",total,"км, машине надо ",days,"дней")

days=(total//one_day+(total%one_day!=0))
print("2.Чтобы проехать",total,"км, машине надо ",days,"дней")