from usecase.notify_after_birth_days_usecase import NotifyAfterBirthDaysUsecase


class NotifyAfterBirthDaysController:
    usecase: NotifyAfterBirthDaysUsecase

    def __init__(self, usecase: NotifyAfterBirthDaysUsecase):
        self.usecase = usecase

    def execute(self):
        success = self.usecase.execute()
        if success:
            return True
        else:
            return False
