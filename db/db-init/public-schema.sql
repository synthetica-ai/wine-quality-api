
CREATE TABLE qualities (
  fixed_acidity real,
  volatile_acidity real,
  citric_acid real,
  residual_sugar real,
  chlorides real,
  free_sulfur_dioxide real,
  total_sulfur_dioxide real,
  density real,
  pH real,
  sulphates real,
  alcohol real
);

\copy qualities(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol) FROM 'winequality.csv' DELIMITER ',' CSV HEADER;
