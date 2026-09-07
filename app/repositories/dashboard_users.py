from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.user import User


class DashboardUserRepository:

    @staticmethod
    def get_total_users(db: Session) -> int:
        return db.query(func.count(User.id)).scalar() or 0

    @staticmethod
    def get_active_users(db: Session) -> int:
        return (
            db.query(func.count(User.id))
            .filter(User.is_active.is_(True))
            .scalar()
            or 0
        )

    @staticmethod
    def get_inactive_users(db: Session) -> int:
        return (
            db.query(func.count(User.id))
            .filter(User.is_active.is_(False))
            .scalar()
            or 0
        )

    @staticmethod
    def get_users_created_after(
        db: Session,
        start_date: datetime
    ) -> int:
        return (
            db.query(func.count(User.id))
            .filter(User.created_at >= start_date)
            .scalar()
            or 0
        )

    @staticmethod
    def get_users_by_role(db: Session) -> dict[str, int]:

        results = (
            db.query(
                User.role,
                func.count(User.id)
            )
            .group_by(User.role)
            .all()
        )

        return {
            role: count
            for role, count in results
        }