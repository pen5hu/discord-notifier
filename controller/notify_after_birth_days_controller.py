from common.result import Result
from usecase.notify_after_birth_days_usecase import NotifyAfterBirthDaysUsecase


class NotifyAfterBirthDaysController:
    usecase: NotifyAfterBirthDaysUsecase

    def __init__(self, usecase: NotifyAfterBirthDaysUsecase):
        self.usecase = usecase

    def execute(self) -> Result[None, Exception]:
        return self.usecase.execute()
