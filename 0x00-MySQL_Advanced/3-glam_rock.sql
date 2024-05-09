-- lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, COALESCE(split, 2022) - formed lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY 2 DESC;
