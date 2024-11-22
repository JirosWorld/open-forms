import {getReactSelectStyles} from '@open-formulieren/formio-builder/esm/components/formio/select';
import classNames from 'classnames';
import {useField} from 'formik';
import PropTypes from 'prop-types';
import ReactSelect from 'react-select';

const initialStyles = getReactSelectStyles();
const styles = {
  ...initialStyles,
  control: (...args) => ({
    ...initialStyles.control(...args),
    minHeight: '1.875rem',
    height: '1.875rem',
  }),
  valueContainer: (...args) => ({
    ...initialStyles.valueContainer(...args),
    height: 'calc(1.875rem - 2px)',
    padding: '0 6px',
  }),
  input: (...args) => ({
    ...initialStyles.input(...args),
    margin: '0px',
  }),
  indicatorsContainer: baseStyles => ({
    ...baseStyles,
    height: 'calc(1.875rem - 2px)',
    padding: '0 2px',
  }),
  dropdownIndicator: (...args) => ({
    ...initialStyles.dropdownIndicator(...args),
    padding: '5px 2px',
  }),
};

/**
 * Find the option by `value` in the list of possible options.
 *
 * `options` are the options passed to ReactSelect, which may be a list of options or
 * a list of option groups: `(Option | Group)[]`. If an item is a group, it has a nested
 * property `options` of type `Option[]`.
 *
 * See https://github.com/JedWatson/react-select/blob/a8b8f4342cc113e921bb238de2dd69a2d345b5f8/packages/react-select/src/Select.tsx#L406
 * for a reference.
 */
const getValue = (options, value) => {
  // 0 could be an actual selected value (!)
  if (value == null || value === '') {
    return null;
  }

  // check all the options until we find a match on the `value` property for the option.
  // ReactSelect allows using different properties for the value, but let's handle that
  // when we actually need it.
  for (const groupOrOption of options) {
    if ('options' in groupOrOption) {
      const hit = getValue(groupOrOption.options, value);
      if (hit) return hit; // otherwise continue with the rest
    } else {
      // we're dealing with a plain option, compare the value property
      if (groupOrOption.value === value) {
        return groupOrOption;
      }
    }
  }

  return null;
};

/**
 * A select dropdown backed by react-select for legacy usage.
 *
 * Any additional props are forwarded to the underlying ReactSelect component.
 *
 * @deprecated - if possible, refactor the form to use Formik and use the Formik-enabled
 * variant.
 */
const SelectWithoutFormik = ({name, options, value, className, onChange, ...props}) => (
  <ReactSelect
    inputId={`id_${name}`}
    name={name}
    className={classNames('admin-react-select', className)}
    classNamePrefix="admin-react-select"
    styles={styles}
    menuPlacement="auto"
    options={options}
    value={getValue(options, value)}
    onChange={selectedOption => {
      onChange(selectedOption === null ? undefined : selectedOption.value);
    }}
    {...props}
  />
);

/**
 * A select dropdown backed by react-select for Formik forms.
 *
 * Any additional props are forwarded to the underlying ReactSelect component.
 */
const SelectWithFormik = ({name, options, className, ...props}) => {
  const [fieldProps, , fieldHelpers] = useField(name);
  const {value} = fieldProps;
  const {setValue} = fieldHelpers;
  return (
    <ReactSelect
      inputId={`id_${name}`}
      className={classNames('admin-react-select', className)}
      classNamePrefix="admin-react-select"
      styles={styles}
      menuPlacement="auto"
      options={options}
      {...fieldProps}
      value={getValue(options, value)}
      onChange={selectedOption => {
        // clear the value
        if (selectedOption == null) {
          setValue(undefined);
        } else {
          setValue(selectedOption.value);
        }
      }}
      {...props}
    />
  );
};

SelectWithoutFormik.propTypes = {
  name: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  options: PropTypes.arrayOf(PropTypes.object),
};

SelectWithFormik.propTypes = {
  name: PropTypes.string.isRequired,
  options: PropTypes.arrayOf(PropTypes.object),
};

export default SelectWithFormik;
export {SelectWithFormik, SelectWithoutFormik};
