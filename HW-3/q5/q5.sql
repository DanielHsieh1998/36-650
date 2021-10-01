ALTER TABLE player_bios
ADD COLUMN position text;

UPDATE player_bios
set position = new_table.position
FROM new_table 
WHERE id = new_table.player;

SELECT firstname, lastname, position 
FROM player_bios
LIMIT 5;