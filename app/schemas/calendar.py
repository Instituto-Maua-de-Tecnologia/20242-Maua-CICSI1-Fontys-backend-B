from pydantic import BaseModel

from app.enum.days_of_week import DayOfWeek


class Calendar(BaseModel):
    calendar_id: str
    professor_id: str
    day_of_week: DayOfWeek
    time_slot: str