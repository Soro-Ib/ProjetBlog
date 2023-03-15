from django.urls import reverse_lazy
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard


class BaseMyDashboard(Dashboard):
    """
    Classe de base pour notre tableau de bord personnalisé
    """

    def init_with_context(self, context):
        """
        Initialise le tableau de bord avec les modules et les options de mise en page
        """
        pass  # À définir dans les classes héritées


class MyIndexDashboard(BaseMyDashboard):
    """
    Tableau de bord personnalisé pour l'index d'administration
    """
    columns = 3

    def init_with_context(self, context):
        super().init_with_context(context)

        self.available_children.append(modules.LinkList)

        link = modules.Link(
            'Aller à ma page personnalisée',
            reverse_lazy('my_custom_page_url')
        )
        self.children.append(link)
