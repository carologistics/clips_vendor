#!/usr/bin/env python
import os
import argparse

NAMESPACE = "clips"

def process_header(input_file_path, output_file_path, namespace):
    """Process header files to add namespace."""
    with open(input_file_path, 'r') as file:
        lines = file.readlines()


    processed_lines = []
    in_namespace = False
    pragma_once_or_guard_processed = False
    include_guard_start = False
    namespace_opened = False
    guard_stack = []

    for line in lines:
        stripped_line = line.strip()

        # Handle include guards
        if stripped_line.startswith("#ifndef") or stripped_line.startswith("#ifdef") or stripped_line.startswith("#if"):
            print("I AM HERE")
            if include_guard_start and not namespace_opened:
                processed_lines.append(f'\nnamespace {namespace} {{\n')
                namespace_opened = True
            if stripped_line.startswith("#ifndef"):
                include_guard_start = True
            guard_stack.append(stripped_line)
            processed_lines.append(line)
            continue

        elif stripped_line.startswith("#endif"):
            if include_guard_start:
                guard_stack.pop()
                if not guard_stack:
                    if namespace_opened:
                        processed_lines.append(f'}} // namespace {namespace}\n')
                        namespace_opened = False
                    include_guard_start = False
            processed_lines.append(line)
            continue

        # Handle #pragma once
        if stripped_line.startswith("#pragma once") and not include_guard_start:
            pragma_once_or_guard_processed = True
            processed_lines.append(line)
            continue

        # Handle #include statements
        if stripped_line.startswith("#include"):
            if namespace_opened:
                processed_lines.append(f'}} // namespace {namespace}\n')
                namespace_opened = False
            processed_lines.append(line)
            continue

        # Add namespace if not already started
        if not namespace_opened and include_guard_start:
            processed_lines.append(f'\nnamespace {namespace} {{\n')
            namespace_opened = True

        processed_lines.append(line)

    # Close the namespace at the end of the file if still open
    if namespace_opened:
        processed_lines.append(f'}} // namespace {namespace}\n')

    with open(output_file_path, 'w') as file:
        file.writelines(processed_lines)

def process_source(input_file_path, output_file_path, namespace):
    """Process source files to add namespace or using namespace."""
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    processed_lines = []

    # Start by opening the namespace
    processed_lines.append(f"namespace {namespace} {{\n")

    in_include_block = False

    for line in lines:
        stripped_line = line.strip()

        # Detect the start of an include block
        if stripped_line.startswith("#include"):
            if not in_include_block:
                # Close the namespace before the include block
                processed_lines.append(f"}} // namespace {namespace}\n")
                in_include_block = True
            processed_lines.append(line)
        else:
            if in_include_block:
                # Reopen the namespace after the include block ends
                processed_lines.append(f"namespace {namespace} {{\n")
                in_include_block = False
            processed_lines.append(line)

    # If the file ends with an include block, make sure to reopen the namespace
    if in_include_block:
        processed_lines.append(f"\nnamespace {namespace} {{\n")

    # Close the namespace at the end of the file
    processed_lines.append(f"}} // namespace {namespace}\n")

    with open(output_file_path, 'w') as file:
        file.writelines(processed_lines)


def preprocess_directory(source_dir, output_dir, namespace):
    """Preprocess all C/C++ files in the given directory."""
    for root, _, files in os.walk(source_dir):
        for file in files:
            input_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_file_path, source_dir)
            output_file_path = os.path.join(output_dir, relative_path)
            
            # Ensure the output directory exists
            output_file_dir = os.path.dirname(output_file_path)
            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir)

            # Process header and source files
            if file.endswith('.h'):
                process_source(input_file_path, output_file_path, namespace)
            elif file.endswith('.c'):
                process_source(input_file_path, output_file_path, namespace)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess C/C++ files by adding namespaces.')
    parser.add_argument('source_dir', help='The directory containing source files to preprocess.')
    parser.add_argument('output_dir', help='The directory where preprocessed files will be saved.')
    parser.add_argument('--namespace', default='clips', help='The namespace to add to the files.')
    args = parser.parse_args()

    preprocess_directory(args.source_dir, args.output_dir, args.namespace)

