#!/usr/bin/env ruby
# Sync labels from .github/labels.yml to a GitHub repository using gh CLI.

require "yaml"
require "open3"
require "optparse"

options = {
  repo: nil,
  file: ".github/labels.yml",
}

OptionParser.new do |opts|
  opts.banner = "Usage: sync_repo_labels.rb [--repo OWNER/REPO] [--file .github/labels.yml]"

  opts.on("--repo REPO", "GitHub repository in OWNER/REPO format") do |value|
    options[:repo] = value
  end

  opts.on("--file FILE", "Path to labels.yml") do |value|
    options[:file] = value
  end
end.parse!

unless File.exist?(options[:file])
  warn "labels file not found: #{options[:file]}"
  exit 1
end

data = YAML.load_file(options[:file])
labels = data["labels"]

unless labels.is_a?(Array)
  warn "invalid labels file: expected top-level 'labels' array"
  exit 1
end

labels.each do |label|
  name = label["name"]
  color = label["color"]
  description = label["description"] || ""

  cmd = ["gh", "label", "create", name, "--color", color, "--description", description, "--force"]
  cmd += ["--repo", options[:repo]] if options[:repo]

  stdout, stderr, status = Open3.capture3(*cmd)
  unless status.success?
    warn stderr.empty? ? stdout : stderr
    exit status.exitstatus || 1
  end
end

puts "synced #{labels.length} labels"
