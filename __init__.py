# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Export2csv
                                 A QGIS plugin
 export coordinates to csv
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-02-28
        copyright            : (C) 2022 by axinav
        email                : axinav
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Export2csv class from file Export2csv.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .export2csv import Export2csv
    return Export2csv(iface)
