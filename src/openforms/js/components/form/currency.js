import {Formio} from 'formiojs';
import CurrencyEditData from 'formiojs/components/currency/editForm/Currency.edit.data';
import _ from 'lodash';

import {ALLOW_NEGATIVE, DECIMAL_PLACES} from './edit/components';
import DEFAULT_TABS, {
  ADVANCED,
  BASIC,
  NUMBER_VALIDATION,
  REGISTRATION,
  TRANSLATIONS,
  VALIDATION,
} from './edit/tabs';
import {localiseSchema} from './i18n';

const FormioCurrency = Formio.Components.components.currency;

CurrencyEditData[0].defaultValue = 'EUR';

class CurrencyField extends FormioCurrency {
  static schema(...extend) {
    return localiseSchema(FormioCurrency.schema(...extend));
  }

  static get builderInfo() {
    return {
      ...FormioCurrency.builderInfo,
      schema: CurrencyField.schema(),
    };
  }

  get defaultValue() {
    let defaultValue = super.defaultValue;

    // Issue #1550: this fix is present in FormIO from v4.14 so can be removed once we upgrade
    if (!this.component.multiple && _.isArray(defaultValue)) {
      defaultValue = !defaultValue[0] && defaultValue[0] !== 0 ? null : defaultValue[0];
    }

    return defaultValue;
  }

  static editForm() {
    const BASIC_TAB = {
      ...BASIC,
      components: [...BASIC.components, ...CurrencyEditData, ...[DECIMAL_PLACES, ALLOW_NEGATIVE]],
    };
    const TABS = {
      ...DEFAULT_TABS,
      components: [BASIC_TAB, ADVANCED, NUMBER_VALIDATION, REGISTRATION, TRANSLATIONS],
    };
    return {components: [TABS]};
  }
}

export default CurrencyField;
