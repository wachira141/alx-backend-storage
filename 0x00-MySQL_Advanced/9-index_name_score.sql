-- Create an index id_name_first_score on the table names
CREATE INDEX idx_name_first_score ON names(name(1), score);
