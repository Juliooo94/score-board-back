import pytest
from unittest.mock import MagicMock, patch
from score_board.user.models import User as CustomUser
from score_board.user.services import log_user_in
from django.test import RequestFactory


@pytest.mark.django_db
class TestLogUserIn:
    def setup_method(self):
        self.factory = RequestFactory()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)

    @patch('score_board.user.services.authenticate')
    def test_log_user_in_authenticated(self, mock_authenticate):
        mock_authenticate.return_value = self.user
        request = self.factory.get('/some-url/')
        request.session = MagicMock()
        request.session.__getitem__.return_value = {}
        request.session.save = MagicMock()

        user = log_user_in(request, self.username, self.password)

        mock_authenticate.assert_called_once_with(request, username=self.username, password=self.password)
        assert user == self.user

    @patch('score_board.user.services.authenticate')  # Corrected patch path
    def test_log_user_in_wrong_password(self, mock_authenticate):
        mock_authenticate.return_value = None

        request = self.factory.get('/some-url/')
        request.session = MagicMock()
        request.session.__getitem__.return_value = {}
        request.session.save = MagicMock()

        with pytest.raises(ValueError, match='Password issue'):
            log_user_in(request, self.username, 'wrongpassword')

    @patch('score_board.user.services.authenticate')
    def test_log_user_in_create_new_user(self, mock_authenticate):
        mock_authenticate.return_value = None

        request = self.factory.get('/some-url/')
        request.session = MagicMock()
        request.session.__getitem__.return_value = {}
        request.session.save = MagicMock()

        new_user = log_user_in(request, 'newuser', self.password)

        assert CustomUser.objects.filter(username='newuser').exists()
        assert new_user.username == 'newuser'
