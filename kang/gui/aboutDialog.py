import sys

from PySide2.QtGui import QPalette, QBrush, QColor, Qt, QFont
from PySide2.QtWidgets import QDialog, QApplication, QDialogButtonBox, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QTabWidget, QWidget, \
    QTextBrowser

from kang import VERSION, KANG_WEBSITE
from kang.images import getIcon, getPixmap

tr = lambda msg: msg


class AboutDialog(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent)

        self.setWindowIcon(getIcon('kang-icon'))
        self.setWindowTitle(tr("About"))
        self.resize(556, 384)
        self.setModal(True)

        verticalLayout = QVBoxLayout()
        verticalLayout.addLayout(self._header())
        verticalLayout.addWidget(self._center())

        buttonBox = QDialogButtonBox(QDialogButtonBox.Close)
        buttonBox.rejected.connect(self.close)

        gridLayout = QGridLayout(self)
        gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)

    def _header(self):

        labelIcon = QLabel()
        iconImage = getPixmap('kang-icon.svg')
        iconImage = iconImage.scaled(64, 64)
        labelIcon.setPixmap(iconImage)

        labelKang = QLabel(tr("KANG"))
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 170))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(170, 0, 170))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(133, 133, 133))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        labelKang.setPalette(palette)
        font = QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        labelKang.setFont(font)

        labelOutline = QLabel(tr("The Python Regular Expression Editor"))

        verticalLayout1 = QVBoxLayout()
        verticalLayout1.addWidget(labelKang)
        verticalLayout1.addWidget(labelOutline)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(labelIcon)
        horizontalLayout.addLayout(verticalLayout1)
        horizontalLayout.addStretch()

        return horizontalLayout

    def _center(self):
        tab1 = QWidget()

        edit = QTextBrowser()
        edit.setReadOnly(True)
        edit.setOpenExternalLinks(True)
        edit.setOpenLinks(True)

        edit.setHtml(GENERAL_HTML)

        layout = QGridLayout(tab1)
        layout.addWidget(edit, 0, 0, 1, 1)

        tab2 = QWidget()

        edit = QTextBrowser()
        edit.setReadOnly(True)
        edit.setOpenExternalLinks(True)
        edit.setOpenLinks(True)

        edit.setHtml(AUTHORS_HTML)

        layout = QGridLayout(tab2)
        layout.addWidget(edit, 0, 0, 1, 1)

        tabWidget = QTabWidget()
        tabWidget.addTab(tab1, tr("General"))
        tabWidget.addTab(tab2, tr("Authors"))

        return tabWidget


GENERAL_HTML = """
<table>
<tr><td>&nbsp;</td><td></td></tr>
<tr><td>%s:&nbsp;</td><td>%s</td></tr>
<tr><td>&nbsp;</td><td></td></tr>
<tr><td>%s:&nbsp;</td><td><a href=\"%s\">%s</a></td></tr>
<tr><td>%s:&nbsp;</td><td><a href=\"http://www.gnu.org/licenses/gpl-3.0.txt\">GNU General Public License v3</a></td></tr>
</table>
""" % (tr("Version"), VERSION,
       tr("Homepage"), KANG_WEBSITE, KANG_WEBSITE,
       tr("License"))

AUTHORS_HTML = """
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
"""

if __name__ == '__main__':
    qApp = QApplication(sys.argv)

    dialog = AboutDialog(None)
    dialog.show()

    sys.exit(qApp.exec_())
