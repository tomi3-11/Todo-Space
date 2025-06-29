# Calendar Utility

import calendar
from datetime import datetime
from calendar import HTMLCalendar

class TaskCalendar(HTMLCalendar):
    def __init__(self, tasks):
        super(HTMLCalendar, self).__init__()
        self.tasks = tasks
        
    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday"></td>'
        
        day_tasks = self.tasks.filter(
            due_date__day=day,
            due_date__year=self.year,
            due_date__month=self.month
        )
        
        task_list = ''
        
        for task in day_tasks:
            title = task.title
            
            # Truncate long task title
            if len(title) > 20:
                title = title[:17] + '...'
                
            # Append each task to the list
            task_list += f'<li title="{task.title}">{title}</li>'
        
        return (
            f'<td class="day" data-date="{self.year}-{self.month:02}-{day:02}">'
            f'<span class="date">{day}</span><ul>{task_list}</ul></td>'
        )
    
    def formatweek(self, theweek):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, weekday)
        return f'<tr>{week}</tr>'
    
    def formatmonth(self, year, month, withyear=True):
        self.year = year
        self.month = month
        
        self.tasks = self.tasks.filter(due_date__year=year, due_date__month=month)
        cal = f'<table class="calendar">\n'
        cal += f'{self.formatmonthname(year, month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(year, month):
            cal += f'{self.formatweek(week)}\n'
        return cal