from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action


from .models import Log
from .serializers import LogSerializer


class LogViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet):
    queryset = Log.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = LogSerializer

    @action(methods=['GET'], detail=False)
    def get_dashboard(self, request, *args, **kwargs):
        """
        Необходимо написать метод, который принимает:
            в качестве обязательного аргумента - ID Channel,
            в качестве необязательных аргументов - дата начала и дата окончания для фильтрации логов.
        Если необязательные аргументы не указаны - фильтровать по умолчанию (три дня назад до сегодня)

        В качестве ответа необходимо отдать логи с дополнительным полем subscribers_diff -
        в этом поле отобразить разницу в количестве подписчиков между текущим днем и предыдущим.
        Пример: У нас в бд есть примерно такие записи:
        -----------------------------------------------------------
        pk  channel_id   created_at   subscribers_count
        1   1            01.01.2020   12
        2   1            02.01.2020   16
        3   1            04.01.2020   21
        4   1            06.01.2020   7
        5   1            07.01.2020   65
        .........

        ------------------------------------------------------------

        После сериализации и обработки верните ответ с дополнительным полем subscribers_diff

        -----------------------------------------------------------
        pk  channel_id   created_at   subscribers_count    subscribers_diff
        1   1            01.01.2020   12                   12
        2   1            02.01.2020   10                   -2
        3   1            04.01.2020   21                   11
        4   1            06.01.2020   7                    -14
        5   1            07.01.2020   65                   58
        .........

        ------------------------------------------------------------

        Обратите внимание на количество обращений в базу данных.
        Возможно для этой задачи понадобится PostgreSQL.
        """