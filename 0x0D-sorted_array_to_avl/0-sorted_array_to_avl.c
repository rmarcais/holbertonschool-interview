#include "binary_trees.h"

/**
 * binary_tree_node - function that creates a binary tree node
 * @parent: a pointer to the parent node of the node to create
 * @value: is the value of the data
 * Return: a pointer to the new node or NULL on failure
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node = malloc(sizeof(binary_tree_t));

	if (new_node == NULL)
		return (NULL);

	new_node->parent = parent;
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->n = value;

	return (new_node);
}

/**
 * build_avl - Builds the tree
 *
 * @array: The array to be converted
 * @start: First index of the array
 * @end: Last index of the array
 * @parent: The parent node
 *
 * Return: A pointer to the root node of the created AVL tree, or NULL.
 */
avl_t *build_avl(int *array, int start, int end, avl_t *parent)
{
	avl_t *new_node;
	size_t middle;

	if (start > end)
		return (NULL);

	middle = (start + end) / 2;

	new_node = binary_tree_node(parent, array[middle]);

	new_node->left = build_avl(array, start, middle - 1, new_node);

	new_node->right = build_avl(array, middle + 1, end, new_node);

	return (new_node);
}

/**
 * sorted_array_to_avl - Function that builds an AVL tree from an array
 *
 * @array: The array to be converted
 * @size: Size of the array
 *
 * Return: A pointer to the root node of the created AVL tree, or NULL.
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
	if (array == NULL || size < 1)
		return (NULL);

	return (build_avl(array, 0, size - 1, NULL));
}
