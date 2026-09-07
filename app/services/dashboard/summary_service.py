class DashboardSummaryService:

    def __init__(self, repository):
        self.repository = repository

    def get_summary(self):
        return {
            "total_employees": self.repository.get_total_employees(),
            "active_employees": self.repository.get_active_employees(),
            "total_forms": self.repository.get_total_forms(),
            "total_submissions": self.repository.get_total_submissions()
        }