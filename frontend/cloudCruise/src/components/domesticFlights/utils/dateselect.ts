function getTodayDateYMD() {
  const calendar = new Date()
  const format = new Intl.DateTimeFormat('en', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  })
  return format.format(calendar)
}

// export function DateFormatter(departureDate: Date) {
//   const day = departureDate.getDate();
//   const month = departureDate.getMonth() + 1;
//   const year = departureDate.getFullYear();

//   return `${year}-${month}-${day}`;
// }

const weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

export function DatesArray(date: string) {
  const dateList = []
  const format = new Intl.DateTimeFormat('en', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  })

  const userDate = new Date(date)
  const getToday = new Date(getTodayDateYMD())

  if (getToday.getDate() === userDate.getDate()) {
    for (let i = 0; i <= 6; i++) {
      let newDate = new Date(userDate)
      const calendar = new Date(newDate)
      calendar.setDate(calendar.getDate() + i)
      newDate = calendar
      let genDate = {
        date: format.format(newDate),
        day: weekday[newDate.getDay()]
      }

      dateList.push(genDate)
    }
  } else {
    const diffInMillisec = userDate.getTime() - getToday.getTime()
    const diffInDays = Math.floor(diffInMillisec / (1000 * 60 * 60 * 24))

    switch (diffInDays) {
      case 1:
        for (let i = -1; i <= 5; i++) {
          let newDate = new Date(userDate)
          const calendar = new Date(newDate)
          calendar.setDate(calendar.getDate() + i)
          newDate = calendar

          let genDate = {
            date: format.format(newDate),
            day: weekday[newDate.getDay()]
          }

          dateList.push(genDate)
        }
        break

      case 2:
        for (let i = -2; i <= 4; i++) {
          let newDate = new Date(userDate)
          const calendar = new Date(newDate)
          calendar.setDate(calendar.getDate() + i)
          newDate = calendar
          let genDate = {
            date: format.format(newDate),
            day: weekday[newDate.getDay()]
          }

          dateList.push(genDate)
        }
        break
      case 3:
        for (let i = -3; i <= 3; i++) {
          let newDate = new Date(userDate)
          const calendar = new Date(newDate)
          calendar.setDate(calendar.getDate() + i)
          newDate = calendar
          let genDate = {
            date: format.format(newDate),
            day: weekday[newDate.getDay()]
          }

          dateList.push(genDate)
        }
        break
      case 4:
        for (let i = -4; i <= 2; i++) {
          let newDate = new Date(userDate)
          const calendar = new Date(newDate)
          calendar.setDate(calendar.getDate() + i)
          newDate = calendar
          let genDate = {
            date: format.format(newDate),
            day: weekday[newDate.getDay()]
          }

          dateList.push(genDate)
        }
        break
      case 5:
        for (let i = -5; i <= 1; i++) {
          let newDate = new Date(userDate)
          const calendar = new Date(newDate)
          calendar.setDate(calendar.getDate() + i)
          newDate = calendar
          let genDate = {
            date: format.format(newDate),
            day: weekday[newDate.getDay()]
          }

          dateList.push(genDate)
        }
        break
      default:
        for (let i = -3; i <= 3; i++) {
          let newDate = new Date(userDate)
          const calendar = new Date(newDate)
          calendar.setDate(calendar.getDate() + i)
          newDate = calendar
          let genDate = {
            date: format.format(newDate),
            day: weekday[newDate.getDay()]
          }

          dateList.push(genDate)
        }
        break
    }
  }

  return dateList
}
