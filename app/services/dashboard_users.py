from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.repositories.dashboard_users import (
    DashboardUserRepository,
)
from app.schemas.dashboard_users import UserStatisticsResponse


class DashboardUserService:

    @staticmethod
    def get_user_statistics(
        db: Session,
    ) -> UserStatisticsResponse:

        now = datetime.utcnow()

        # Start of today
        start_of_today = datetime(
            now.year,
            now.month,
            now.day
        )

        # Start of current week
        start_of_week = start_of_today - timedelta(
            days=start_of_today.weekday()
        )

        # Start of current month
        start_of_month = datetime(
            now.year,
            now.month,
            1
        )

        total_users = (
            DashboardUserRepository
            .get_total_users(db)
        )

        active_users = (
            DashboardUserRepository
            .get_active_users(db)
        )

        inactive_users = (
            DashboardUserRepository
            .get_inactive_users(db)
        )

        new_users_today = (
            DashboardUserRepository
            .get_users_created_after(
                db,
                start_of_today
            )
        )

        new_users_this_week = (
            DashboardUserRepository
            .get_users_created_after(
                db,
                start_of_week
            )
        )

        new_users_this_month = (
            DashboardUserRepository
            .get_users_created_after(
                db,
                start_of_month
            )
        )

        users_by_role = (
            DashboardUserRepository
            .get_users_by_role(db)
        )

        if total_users > 0:
            active_percentage = round(
                (active_users / total_users) * 100,
                2
            )
        else:
            active_percentage = 0.0

        return UserStatisticsResponse(
            total_users=total_users,
            active_users=active_users,
            inactive_users=inactive_users,
            active_percentage=active_percentage,
            new_users_today=new_users_today,
            new_users_this_week=new_users_this_week,
            new_users_this_month=new_users_this_month,
            users_by_role=users_by_role,
        )