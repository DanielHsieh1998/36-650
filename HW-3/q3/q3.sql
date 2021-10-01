CREATE TYPE DivisionType AS ENUM ('Atlantic', 'Central','Southeast',
								 'Northwest', 'Pacific','Southwest')
CREATE TYPE ConferenceType AS ENUM ('Eastern', 'Western')

CREATE TABLE teams(
	id char(3) PRIMARY KEY,
	location text,	
	name text,
	division DivisionType,
	conference ConferenceType
);