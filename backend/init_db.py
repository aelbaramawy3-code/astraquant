from app.database.base import Base
from app.database.connection import engine

# استيراد جميع الـ Models هنا
from app.models.user import User

Base.metadata.create_all(bind=engine)

print("✅ Database tables created successfully.")