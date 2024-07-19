from qfluentwidgets import qrouter, FluentIcon

from one_dragon.gui.component.interface.pivot_navi_interface import PivotNavigatorInterface
from one_dragon.gui.view.setting.setting_env_interface import SettingEnvInterface
from zzz_od.context.zzz_context import ZContext
from zzz_od.gui.view.setting.setting_game_interface import SettingGameInterface


class AppSettingInterface(PivotNavigatorInterface):

    def __init__(self, ctx: ZContext, parent=None):
        PivotNavigatorInterface.__init__(self, ctx=ctx, object_name='app_setting_interface', parent=parent,
                                         nav_text_cn='设置', nav_icon=FluentIcon.SETTING)

        self.add_sub_interface(SettingEnvInterface(ctx=ctx))
        self.add_sub_interface(SettingGameInterface(ctx=ctx))
        qrouter.setDefaultRouteKey(self.stacked_widget, self.stacked_widget.currentWidget().objectName())

    def on_interface_shown(self) -> None:
        """
        子界面显示时 进行初始化
        :return:
        """
        self.stacked_widget.currentWidget().on_interface_shown()