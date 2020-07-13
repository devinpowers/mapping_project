#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Map Practice
@author: devinpowers
"""
import folium

# create map object

m = folium.Map(location=[42.963795, -85.670006], zoom_start=12)

# Global Tooltip

tooltip = 'Click For More Info'

# Creat markers

folium.Marker([43.033290,-85.651440 ], 
              popup ='<strong> Devins Crib </strong>',
              tooltip = tooltip).add_to(m)
                                  
# Generate Map

m.save('map3.html')

