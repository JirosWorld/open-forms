import React, {useContext} from 'react';
import PropTypes from 'prop-types';
import {useIntl} from 'react-intl';

import Select from '../../forms/Select';
import DeleteIcon from '../../DeleteIcon';
import {ACTION_TYPES, ACTIONS_WITH_OPTIONS, MODIFIABLE_PROPERTIES, PROPERTY_VALUES, STRING_TO_TYPE} from './constants';
import ComponentSelection from './ComponentSelection';
import LiteralValueInput from './LiteralValueInput';
import {ComponentsContext} from './Context';
import OperandTypeSelection from './OperandTypeSelection';
import DataPreview from './DataPreview';


const Action = ({prefixText, action, onChange, onDelete}) => {
    const intl = useIntl();
    const allComponents = useContext(ComponentsContext);
    const componentType = allComponents[action.componentToChange]?.type;

    const jsonAction = {
        component: action.componentToChange,
        action: {
            type: action.actionType,
            property: {value: action.componentProperty, type: action.componentPropertyType},
            // The data in 'value' needs to be valid jsonLogic
            value: action.componentLiteralValue || {var: action.componentVariableValue},
            state: action.componentPropertyValue,
        }
    };

    // apply i18n to the constants choice labels
    const actionTypeChoices = ACTION_TYPES.map( ([value, msg]) => [value, intl.formatMessage(msg)] );
    const modifiablePropertyChoices = Object.entries(MODIFIABLE_PROPERTIES).map(
        ([key, info]) => [key, intl.formatMessage(info.label)]
    );
    const propertyValueChoices = PROPERTY_VALUES.map( ([value, msg]) => [value, intl.formatMessage(msg)] );

    return (
        <div className="logic-action">

            <div className="logic-action__actions">
                <DeleteIcon
                    onConfirm={onDelete}
                    message={intl.formatMessage({
                        description: 'Logic rule action deletion confirm message',
                        defaultMessage: 'Are you sure you want to delete this action?',
                    })}
                />
            </div>

            <div className="logic-action__action">
                <div className="dsl-editor">
                    <div className="dsl-editor__node">{prefixText}</div>

                    <div className="dsl-editor__node">
                        <Select
                            name="actionType"
                            choices={actionTypeChoices}
                            allowBlank
                            onChange={onChange}
                            value={action.actionType}
                        />
                    </div>

                    {
                        ACTIONS_WITH_OPTIONS.includes(action.actionType)
                        ? (
                            <div className="dsl-editor__node">
                                <ComponentSelection
                                    name="componentToChange"
                                    value={action.componentToChange}
                                    onChange={onChange}
                                />
                            </div>
                        )
                        : null
                    }
                    {
                        action.actionType === 'property'
                        ? (
                            <>
                                <div className="dsl-editor__node">
                                    <Select
                                        name="componentProperty"
                                        choices={modifiablePropertyChoices}
                                        allowBlank
                                        onChange={(event) => {
                                            const property = event.target.value;
                                            onChange(event);
                                            onChange({
                                                target: {
                                                    name: 'componentPropertyType',
                                                    value: MODIFIABLE_PROPERTIES[property].type
                                                }
                                            });
                                        }}
                                        value={action.componentProperty}
                                    />
                                </div>
                                <div className="dsl-editor__node">
                                    <Select
                                        name="componentPropertyValue"
                                        choices={propertyValueChoices}
                                        allowBlank
                                        onChange={(event) => {
                                            const propertyType = action.componentPropertyType;
                                            const propertyValue = STRING_TO_TYPE[propertyType](event.target.value);
                                            onChange({
                                                target: {
                                                    name: 'componentPropertyValue',
                                                    value: propertyValue
                                                }
                                            })
                                        }}
                                        value={action.componentPropertyValue ? String(action.componentPropertyValue) : action.componentPropertyValue}
                                    />
                                </div>
                            </>
                        )
                        : null
                    }
                    {
                        // Used to pick whether the new value of a component will be a literal or a value from another component
                        action.actionType === 'value'
                        ? (
                            <div className="dsl-editor__node">
                                <OperandTypeSelection
                                    name="componentValueSource"
                                    onChange={onChange}
                                    operandType={action.componentValueSource}
                                />
                            </div>
                        )
                        : null
                    }
                    {
                        action.actionType === 'value' && action.componentValueSource === 'literal'
                        ? (
                            <div className="dsl-editor__node">
                                <LiteralValueInput
                                    name="componentLiteralValue"
                                    componentType={componentType}
                                    value={action.componentLiteralValue}
                                    onChange={onChange}
                                />
                            </div>
                        )
                        : null
                    }
                    {
                        action.actionType === 'value' && action.componentValueSource === 'component'
                        ? (
                            <div className="dsl-editor__node">
                                <ComponentSelection
                                    name="componentVariableValue"
                                    value={action.componentVariableValue}
                                    onChange={event => {
                                        const fakeEvent = {target: {name: 'componentLiteralValue', value: ''}};
                                        onChange(fakeEvent);
                                        onChange(event);
                                    }}
                                    filter={(comp) => (comp.type === componentType)}
                                />
                            </div>
                        )
                        : null
                    }

                </div>
            </div>

            <div className="logic-action__data-preview">
                <DataPreview data={jsonAction} />
            </div>

        </div>
    );
};

Action.propTypes = {
    prefixText: PropTypes.node.isRequired,
    action: PropTypes.object.isRequired,
    onChange: PropTypes.func.isRequired,
    onDelete: PropTypes.func.isRequired,
};

export default Action;