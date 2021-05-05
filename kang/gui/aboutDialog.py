from kang import KANG_WEBSITE
from kang import VERSION
from kang.gui.aboutDialogBA import Ui_AboutDialogBA
from kang.images import getPixmap, getIcon


class AboutDialog(Ui_AboutDialogBA):

    def __init__(self, parent):
        Ui_AboutDialogBA.__init__(self, parent)
        self.parent = parent

        self.setWindowIcon(getIcon('kang-icon'))

        bugImage = getPixmap("kang-icon.svg")
        bugImage = bugImage.scaled(64, 64)

        self.labelIcon.setPixmap(bugImage)

        self.label_versiontxt.setText(VERSION)

        self.label_homepagetxt.setText('<a href=\"%s\">%s</a>' % (KANG_WEBSITE, KANG_WEBSITE))
        self.label_homepagetxt.setOpenExternalLinks(True)

        self.label_licensetxt.setText('<a href=\"http://www.gnu.org/licenses/gpl-2.0.txt\">GNU General Public License v2</a>')
        self.label_licensetxt.setOpenExternalLinks(True)

        self.textAuthors.setText("""
<b>Maintainer / Lead Developer</b>
<ul>
<li>Alessio Piccoli &lt;alepic@geckoblu.net&gt;</li>
</ul>
<p>&nbsp;</p>
<p>
<b>Kodos</b><br/>
Kang is a fork of <a href="http://kodos.sourceforge.net">Kodos</a>.<br/>
Original credits for Kodos are:
<ul>
<li>Developed by: Phil Schwartz &lt;phil_schwartz@users.sourceforge.net&gt;</li>
<li>Logo designed by: Konstantin Ryabitsev &lt;icon@fedoraproject.org&gt;</li>
</ul>

</p>
""")
