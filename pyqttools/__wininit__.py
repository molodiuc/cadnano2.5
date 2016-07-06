# Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt5.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Added NC to add the Library path

import sys
import os.path
from .QtCore import QCoreApplication
LOCAL_QT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Qt')
QCoreApplication.addLibraryPath(os.path.join(LOCAL_QT, 'plugins'))