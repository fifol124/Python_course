print('Podaj swoją masę ciała: ')
mass=input()
print('Podaj swój wzrost w metrach (1.Xm): ')
height=input()


mass=float(mass)
height=float(height)
BMI=(mass/height**2)
BMI_round=round(BMI,3)
print('Twoje BMI to ' +str(float(BMI_round)))