t = int(input("enter seconds"))
days = t / 86400
hours = int((t % 86400)/3600)
minutes = int((t % 86400) % 3600)/60
second = int((((t % 86400) % 3600) % 60))
print("\n", t, "second = ", (days), "days", (hours), "hours", (minutes), "minutes", (second), "seconds")