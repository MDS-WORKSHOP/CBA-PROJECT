from langchain_core.messages import HumanMessage
from typing import List, Optional,Dict
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

from llms import (
    get_openai_llm,
    get_embedding_openai,
)

class DynamicSpecification(BaseModel):
    details: Dict[str, str] = Field(default={}, description="Details of specifications like range, accuracy, resolution. Example: 'DC Voltage: 300mV-1000V, ±0.025% + 2, 1 µV-0.01V'")
    
class DynamicCharacteristics(BaseModel):
    details: Dict[str, str] = Field(default={}, description="Details of characteristics like display type, size, weight, dimensions. Example: 'Display Type: TFT LCD, Display Size: 5.7 inches, Weight: 2 kg'")

class InstrumentCharacteristics(BaseModel):
    name: Optional[str] = Field(default=None, description="The name of the instrument")
    part_number: Optional[str] = Field(default=None, description="Part number of the instrument")
    manufacturer: Optional[str] = Field(default=None, description="Manufacturer of the instrument")
    specifications: Optional[DynamicSpecification] = Field(default=None, description="General specifications of the instrument")
    characteristics: Optional[DynamicCharacteristics] = Field(default=None, description="General characteristics of the instrument")
    performance: Optional[List[str]] = Field(default=None, description="Performance characteristics of the instrument")
    physical: Optional[List[str]] = Field(default=None, description="Physical characteristics of the instrument")
    input_output: Optional[List[str]] = Field(default=None, description="Input/Output characteristics of the instrument")
    software: Optional[List[str]] = Field(default=None, description="Software characteristics of the instrument")
    other: Optional[List[str]] = Field(default=None, description="Other characteristics of the instrument")
    display: Optional[List[str]] = Field(default=None, description="Display characteristics of the instrument")
    comments: Optional[List[str]] = Field(default=None, description="Additional comments about the instrument")

class DigitizingSignalOscilloscope(InstrumentCharacteristics):
    bandwidth: Optional[str] = Field(default=None, description="Bandwidth of the oscilloscope")
    channels: Optional[str] = Field(default=None, description="Number of channels")
    sample_rate: Optional[str] = Field(default=None, description="Sample rate on each channel")
    record_length: Optional[str] = Field(default=None, description="Record length on all models")
    vertical_resolution: Optional[str] = Field(default=None, description="Vertical resolution")
    vertical_sensitivity: Optional[str] = Field(default=None, description="Vertical sensitivity")
    dc_vertical_accuracy: Optional[str] = Field(default=None, description="DC vertical accuracy")
    max_input_voltage: Optional[str] = Field(default=None, description="Maximum input voltage")
    time_base_range: Optional[str] = Field(default=None, description="Time base range")
    time_base_accuracy: Optional[str] = Field(default=None, description="Time base accuracy")
    horizontal_zoom: Optional[str] = Field(default=None, description="Horizontal zoom")
    io_interfaces: Optional[List[str]] = Field(default=None, description="Input/Output interfaces")
    acquisition_modes: Optional[List[str]] = Field(default=None, description="Acquisition modes")
    trigger_system: Optional[List[str]] = Field(default=None, description="Trigger system characteristics")
    cursors: Optional[List[str]] = Field(default=None, description="Cursor characteristics")
    automatic_waveform_measurements: Optional[List[str]] = Field(default=None, description="Automatic waveform measurements")
    waveform_math: Optional[List[str]] = Field(default=None, description="Waveform math operations")
    autoset_menu: Optional[List[str]] = Field(default=None, description="Autoset menu options")
    display_characteristics: Optional[List[str]] = Field(default=None, description="Display characteristics")
    environmental_safety: Optional[List[str]] = Field(default=None, description="Environmental and safety characteristics")

class ACPowerSupply(InstrumentCharacteristics):
    frequency_range: Optional[str] = Field(default=None, description="Frequency range of the power supply")
    voltage_reference: Optional[str] = Field(default=None, description="Voltage reference")
    output_voltage_range: Optional[str] = Field(default=None, description="Output voltage range")
    output_current: Optional[str] = Field(default=None, description="Output current")
    current_limit: Optional[str] = Field(default=None, description="Current limit")
    line_regulation: Optional[str] = Field(default=None, description="Line regulation")

class DCLoad(InstrumentCharacteristics):
    constant_current_range: Optional[str] = Field(default=None, description="Range for constant current")
    current_accuracy: Optional[str] = Field(default=None, description="Accuracy of the current")
    max_voltage_power: Optional[str] = Field(default=None, description="Maximum voltage and power")
    short_circuit_current: Optional[str] = Field(default=None, description="Short circuit current")
    measurement_accuracy: Optional[List[str]] = Field(default=None, description="Measurement accuracy for voltage and current")


class DigitalMultimeter(InstrumentCharacteristics):
    voltage_range: Optional[str] = Field(default=None, description="Voltage range")
    resolution: Optional[str] = Field(default=None, description="Resolution")
    accuracy: Optional[str] = Field(default=None, description="Accuracy")
    dc_voltage_measurement: Optional[str] = Field(default=None, description="DC voltage measurement details")
    ac_voltage_measurement: Optional[str] = Field(default=None, description="AC voltage measurement details")
    signal_sampling: Optional[List[str]] = Field(default=None, description="Details on DC and AC signal sampling")
    frequency_measurement_range: Optional[str] = Field(default=None, description="Frequency measurement range")

class ProgrammableFunctionGenerator(InstrumentCharacteristics):
    amplitude_range: Optional[List[str]] = Field(default=None, description="Amplitude range details")
    offset_range: Optional[List[str]] = Field(default=None, description="Offset range details")
    frequency_range: Optional[List[str]] = Field(default=None, description="Frequency range details")
    sine_distortion: Optional[List[str]] = Field(default=None, description="Sine distortion details")
    pulse_width: Optional[List[str]] = Field(default=None, description="Pulse width details")

class SynchroResolverModule(InstrumentCharacteristics):
    angle_range: Optional[str] = Field(default=None, description="Programmable angle range")
    reference_input: Optional[List[str]] = Field(default=None, description="Reference input characteristics")
    output_characteristics: Optional[List[str]] = Field(default=None, description="Output characteristics")
    angle_measurement_range: Optional[str] = Field(default=None, description="Measured angle position range")
    input_characteristics: Optional[List[str]] = Field(default=None, description="Input characteristics")

class OpticalAttenuator(InstrumentCharacteristics):
    wavelength_range: Optional[str] = Field(default=None, description="Wavelength range")
    attenuation_range: Optional[str] = Field(default=None, description="Attenuation range")
    insertion_loss: Optional[str] = Field(default=None, description="Insertion loss")
    fibre_type: Optional[str] = Field(default=None, description="Fibre type")
    connector_type: Optional[str] = Field(default=None, description="Connector type")

class OpticalSwitch(InstrumentCharacteristics):
    wavelength_range: Optional[str] = Field(default=None, description="Wavelength range")
    fibre_type: Optional[str] = Field(default=None, description="Fibre type")
    insertion_loss: Optional[str] = Field(default=None, description="Insertion loss")
    bidirectional_switch: Optional[bool] = Field(default=None, description="Bidirectional switch availability")

class OpticalPowermeter(InstrumentCharacteristics):
    wavelength_range: Optional[str] = Field(default=None, description="Wavelength range")
    power_range: Optional[str] = Field(default=None, description="Power range")
    fibre_type: Optional[str] = Field(default=None, description="Fibre type")

class VideoPatternGenerator(InstrumentCharacteristics):
    interface: Optional[List[str]] = Field(default=None, description="Interface details")
    parameters: Optional[List[str]] = Field(default=None, description="Parameters")
    pattern: Optional[List[str]] = Field(default=None, description="Pattern generation details")

class HighLevelPressureGenerator(InstrumentCharacteristics):
    pressure_supply: Optional[str] = Field(default=None, description="Pressure supply input details")
    vacuum_supply: Optional[str] = Field(default=None, description="Vacuum supply input details")
    input_output_ports: Optional[List[str]] = Field(default=None, description="Input/output ports details")
    pressure_range: Optional[List[str]] = Field(default=None, description="Pressure range details")
    pressure_generation_measurement: Optional[List[str]] = Field(default=None, description="Pressure generation and measurement details")
    accuracy: Optional[str] = Field(default=None, description="Accuracy details")

class LowLevelPressureGenerator(InstrumentCharacteristics):
    pressure_supply: Optional[str] = Field(default=None, description="Pressure supply input details")
    vacuum_supply: Optional[str] = Field(default=None, description="Vacuum supply input details")
    input_output_ports: Optional[List[str]] = Field(default=None, description="Input/output ports details")
    pressure_range: Optional[List[str]] = Field(default=None, description="Pressure range details")
    pressure_generation_measurement: Optional[List[str]] = Field(default=None, description="Pressure generation and measurement details")
    accuracy: Optional[str] = Field(default=None, description="Accuracy details")

def extract_information(file_path, schema):
    model = get_openai_llm(gpt_4=True, azure=False)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert extraction algorithm. Only extract relevant information from the text "
                "Only extract characteristic and specifications about product. Extract nothing if no important information can be found in the text.",
            ),
            ("human", "{text}"),
        ]
    )

    # Dynamically select schema based on user input
    schema_mapping = {
        "DigitizingSignalOscilloscope": DigitizingSignalOscilloscope,
        "ACPowerSupply": ACPowerSupply,
        "DCLoad": DCLoad,
        "DigitalMultimeter": DigitalMultimeter,
        "ProgrammableFunctionGenerator": ProgrammableFunctionGenerator,
        "SynchroResolverModule": SynchroResolverModule,
        "OpticalAttenuator": OpticalAttenuator,
        "OpticalSwitch": OpticalSwitch,
        "OpticalPowermeter": OpticalPowermeter,
        "VideoPatternGenerator": VideoPatternGenerator,
        "HighLevelPressureGenerator": HighLevelPressureGenerator,
        "LowLevelPressureGenerator": LowLevelPressureGenerator
    }

    extractor = prompt | model.with_structured_output(schema=schema_mapping.get(schema, InstrumentCharacteristics))

    loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embedding_function = get_embedding_openai()

    vector_db = Chroma.from_documents(docs, embedding_function)
    retriever = vector_db.as_retriever(search_kwargs={"k": 6})

    rag_extractor = {
        "text": retriever  # fetch content of top doc
    } | extractor

    extractor_prompt = (
        "Please extract all relevant specifications and characteristics of the product in tables. "
        "I need detailed information on the following aspects: voltage, current, resistance, power, frequency, "
        "temperature, humidity, pressure, weight, dimensions, Sample Rate on Each Channel, and any other pertinent characteristics "
        "that describe the product's performance and physical attributes."
    )

    results = rag_extractor.invoke(extractor_prompt)
    return results