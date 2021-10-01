ALTER TABLE player_bios
ADD COLUMN sim_h numeric;

UPDATE player_bios
set sim_h = 12*split_part(height,'-',1)::integer + 
	split_part(height,'-',2)::integer

ALTER TABLE player_bios
	DROP COLUMN height;
	
ALTER TABLE player_bios
	RENAME COLUMN sim_h TO height;

SELECT firstname, lastname, height
FROM player_bios
LIMIT 5;