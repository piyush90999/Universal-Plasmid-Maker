# Universal Plasmid Maker

A bioinformatics pipeline designed to mine the Origin of Replication (ORI) from an unknown organism's genome and assemble a functional plasmid based on user-defined parts.

## 🧬 Project Overview

This tool automates the creation of a plasmid sequence by:

1. **Mining the ORI**: Using **GC Skew Analysis** to identify the replication origin in an unknown input sequence (e.g., `pUC19.fa`).
2. 
**Part Selection**: Retrieving DNA sequences for restriction sites and markers from a provided database (`markers.tab`).


3. **Custom Assembly**: Constructing the plasmid according to a design file (`Design.txt`).
4. **Site Exclusion**: Specifically handling the removal of sequences (like **EcoRI**) if they are omitted from the design specifications.

## 📁 Repository Structure

* `main.py`: The orchestrator script that handles input/output and FASTA formatting.
* `src/`:
* `ori_finder.py`: Algorithmic logic for detecting the ORI minima.
* `assembler.py`: Logic for stitching parts together and excluding unwanted sites.
* 
`database.py`: Mapping for enzyme sequences (e.g., BamHI, HindIII) and marker genes.




* `data/`: Contains `pUC19.fa`, `Design_pUC19.txt`, and `markers.tab`.

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* No external libraries (like Matplotlib) are required for the core pipeline.

### Installation

```bash
git clone https://github.com/YourUsername/Universal-Plasmid-Maker.git
cd Universal-Plasmid-Maker

```

### Running the Tool

To generate the plasmid from the provided test files:

```bash
python main.py -i data/pUC19.fa -d data/Design_pUC19.txt

```

## 🧪 The pUC19 Test Case

The challenge required that the output plasmid **not** contain the **EcoRI** site (`GAATTC`), which is present in the original `pUC19.fa` sequence.

* **Input**: `pUC19.fa` (contains EcoRI at index 283).
* **Design**: `Design_pUC19.txt` lists multiple sites (BamHI, HindIII, PstI, etc.) but **excludes** EcoRI.
* **Result**: The tool assembles the new sequence using only requested parts and the mined ORI. Because EcoRI was not in the design, it is successfully "deleted" from the final construct.

## 📄 Output Format

The tool generates a dynamically named FASTA file (e.g., `pUC19_Output.Fa`). The DNA sequence is wrapped to **80 characters per line** for standard bioinformatics compatibility.

---
