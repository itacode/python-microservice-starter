from app.api.controller.health_controller import get_health


class TestHealthController:
    def test_get_health(self):
        assert get_health() == "OK"
