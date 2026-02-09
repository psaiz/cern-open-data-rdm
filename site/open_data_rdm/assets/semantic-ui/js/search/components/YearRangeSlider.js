
import React, { useState } from 'react';
import { Range } from 'rc-slider';
import 'rc-slider/assets/index.css';
import { Segment, Header } from 'semantic-ui-react';



const YearRangeSlider = ({ minYear = 1950, maxYear = 2025, onChange }) => {
  const [range, setRange] = useState([1953, 2010]);

  const handleChange = (newRange) => {
    setRange(newRange);
    if (onChange) onChange(newRange);
  };

  return (
    <Segment>
      <Header as="h4">Year Range: {range[0]} – {range[1]}</Header>
      <Range
        min={minYear}
        max={maxYear}
        defaultValue={range}
        onChange={handleChange}
        trackStyle={[{ backgroundColor: '#2185d0' }]} // Semantic UI blue
        handleStyle={[
          { borderColor: '#2185d0' },
          { borderColor: '#2185d0' },
        ]}
      />
    </Segment>
  );
};

export default YearRangeSlider;