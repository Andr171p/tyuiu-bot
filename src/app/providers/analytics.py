from dishka import Provider, Scope, provide

from src.services.analytics import AnalyticsService


class AnalyticsProvider(Provider):
    @provide(scope=Scope.APP)
    def get_analytics_service(self) -> AnalyticsService:
        return AnalyticsService()
