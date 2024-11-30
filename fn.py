def checkTime(time: str) -> bool:
  try:
    time1, time2 = time.split()
    day, month, year = map(int, time1.split('.'))
    hour, minutes = map(int, time2.split(':'))
    return day >= 1 and day <= 31 and month >= 1 and month <= 12 and hour >= 0 and hour <= 23 and minutes >= 0 and minutes <= 59
  except:
    return False