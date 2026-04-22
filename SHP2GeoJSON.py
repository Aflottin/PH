import geopandas as gpd

def SHP2GeoJSON(ShpPath, GeoJSONPath):
    
    gdf = gpd.read_file(ShpPath)

    print(gdf.columns)
    print("CRS:", gdf.crs)

    gdf = gdf.to_crs(epsg=4326)

    gdf.to_file(GeoJSONPath, driver="GeoJSON")
